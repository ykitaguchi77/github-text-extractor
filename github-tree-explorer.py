import SwiftUI

@main
struct DynamicAllocation: App {
    let persistenceController = PersistenceController.shared
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}


import SwiftUI


struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink(destination: InputView()) {
                    Text("入力画面")
                }
                NavigationLink(destination: SubjectListView()) {
                    Text("CoreData閲覧ページ")
                }
            }
            .navigationTitle("動的割り付けアプリ")
        }
    }
}


//
//  InputView.swift
//  DynamicAllocation
//
//  Created by Yoshiyuki Kitaguchi on 2024/03/14.
//

import SwiftUI

struct InputView: View {
    @Environment(\.managedObjectContext) private var viewContext
    
    @State private var id = ""
    @State private var gender = "男性"
    @State private var age = "50歳未満"
    @State private var hasTrick = "あり"
    @State private var assignment = ""
    
    var body: some View {
        Form {
            TextField("ID", text: $id)
            
            Picker("性別", selection: $gender) {
                Text("男性").tag("男性")
                Text("女性").tag("女性")
            }
            .pickerStyle(SegmentedPickerStyle())
            
            Picker("年齢", selection: $age) {
                Text("50歳未満").tag("50歳未満")
                Text("50歳以上").tag("50歳以上")
            }
            .pickerStyle(SegmentedPickerStyle())
            
            Picker("知覚トリック", selection: $hasTrick) {
                Text("あり").tag("あり")
                Text("なし").tag("なし")
            }
            .pickerStyle(SegmentedPickerStyle())
            
            Button("組み入れ") {
                assignSubject()
            }
            
            Text("組み入れ結果: \(assignment)")
        }
        .navigationTitle("入力画面")
    }
    
    private func assignSubject() {
        // 動的割り付けのロジックを実装
        // ...
        
        let newSubject = Subject(context: viewContext)
        newSubject.id = id
        newSubject.gender = gender
        newSubject.age = age
        newSubject.hasTrick = hasTrick == "あり" // 文字列からBool値に変換
        newSubject.assignment = assignment
        
        do {
            try viewContext.save()
        } catch {
            print("Failed to save subject: \(error)")
        }
    }
}



import SwiftUI
struct SubjectListView: View {
    @Environment(\.managedObjectContext) private var viewContext
    
    @FetchRequest(
        sortDescriptors: [NSSortDescriptor(keyPath: \Subject.id, ascending: true)],
        animation: .default)
    private var subjects: FetchedResults<Subject>
    
    var body: some View {
        List {
            ForEach(subjects) { subject in
                VStack(alignment: .leading) {
                    Text("ID: \(subject.id)")
                    Text("性別: \(subject.gender)")
                    Text("年齢: \(subject.age)")
                    Text("知覚トリック: \(subject.hasTrick ? "あり" : "なし")")
                    Text("割り付け: \(subject.assignment)")
                }
            }
        }
        .navigationTitle("CoreData閲覧ページ")
    }
}



import Foundation
import CoreData

@objc(Subject)
public class Subject: NSManagedObject, Identifiable {
    @NSManaged public var id: String
    @NSManaged public var gender: String
    @NSManaged public var age: String
    @NSManaged public var hasTrick: Bool
    @NSManaged public var assignment: String
}





import Foundation
import CoreData

@objc(Item)
public class Item: NSManagedObject {

}


import Foundation
import CoreData


extension Item {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<Item> {
        return NSFetchRequest<Item>(entityName: "Item")
    }

    @NSManaged public var age: String?
    @NSManaged public var assignment: String?
    @NSManaged public var gender: String?
    @NSManaged public var hasTrick: Bool
    @NSManaged public var id: String?

}

extension Item : Identifiable {

}


import CoreData

struct PersistenceController {
    static let shared = PersistenceController()

    let container: NSPersistentContainer

    init() {
        container = NSPersistentContainer(name: "DynamicAllocation")
        container.loadPersistentStores { (storeDescription, error) in
            if let error = error as NSError? {
                fatalError("Unresolved error \(error), \(error.userInfo)")
            }
        }
    }
}
